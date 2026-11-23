// Display-only cleanup for directory names: decode HTML entities such as &ndash;
// and drop a trailing date range, since the dates are appended once after the link.
function decodeEntities(v) {
  var t = document.createElement("textarea");
  t.innerHTML = v || "";
  return t.value;
}
function displayName(x) {
  var n = decodeEntities(x.name);
  if (x.born || x.died) n = n.replace(/\s*\(\s*[\d?]{0,4}\s*[\u2013-]\s*[\d?]{0,4}\s*\)\s*$/, "");
  return n;
}

// Tufts Lineage & Legacy site script. Asset paths are built from ASSET_BASE_URL (config.js).
function assetUrl(path) {
  return ASSET_BASE_URL.replace(/\/$/, "") + "/" + path.replace(/^\//, "");
}
document.addEventListener("DOMContentLoaded", function () {
  var y = document.getElementById("year");
  if (y) y.textContent = new Date().getFullYear();
});

// People index: search plus era and line filters, driven by data/people.json.
function initPeople() {
  var list = document.getElementById("people-list");
  if (!list) return;
  var q = document.getElementById("q"), era = document.getElementById("era"), line = document.getElementById("line");
  fetch("data/people.json").then(function (r) { return r.json(); }).then(function (people) {
    people.sort(function (a, b) { return a.name.localeCompare(b.name); });
    [["era", era], ["line", line]].forEach(function (p) {
      Array.from(new Set(people.map(function (x) { return x[p[0]]; }).filter(Boolean))).sort().forEach(function (v) {
        var o = document.createElement("option"); o.value = v; o.textContent = decodeEntities(v); p[1].appendChild(o);
      });
    });
    function render() {
      var t = q.value.trim().toLowerCase();
      var rows = people.filter(function (x) {
        return (!t || x.name.toLowerCase().indexOf(t) > -1) && (!era.value || x.era === era.value) && (!line.value || x.line === line.value);
      });
      list.innerHTML = "";
      if (!rows.length) {
        list.innerHTML = '<p class="note">' + (people.length ? "No matching people." : "No people have been published yet. Profiles are added only after each is checked against its sources.") + "</p>";
        return;
      }
      var ul = document.createElement("ul");
      rows.forEach(function (x) {
        var li = document.createElement("li"), a = document.createElement("a");
        a.href = x.profile; a.textContent = displayName(x);
        if (x.rw === "musket" || x.rw === "pistol") {
          var img = document.createElement("img");
          img.className = "rw-icon";
          img.src = assetUrl("icons/" + x.rw + ".svg");
          img.alt = "";
          img.width = 22;
          img.height = 10;
          var label = x.rw === "musket"
            ? "Revolutionary War service: extensive"
            : "Revolutionary War service: limited service or support of the war effort";
          img.title = label;
          img.setAttribute("aria-label", label);
          a.appendChild(img);
        }
        li.appendChild(a);
        li.appendChild(document.createTextNode(" (" + (x.born || "?") + "–" + (x.died || "?") + ")" + (x.era ? " · " + decodeEntities(x.era) : "") + (x.line ? " · " + decodeEntities(x.line) : "")));
        ul.appendChild(li);
      });
      list.appendChild(ul);
    }
    [q, era, line].forEach(function (el) { el.addEventListener("input", render); });
    render();
  }).catch(function () { list.innerHTML = '<p class="note">The people index could not be loaded.</p>'; });
}

// Page scans gallery, driven by data/sources.json.
function initScans() {
  var box = document.getElementById("scan-list");
  if (!box) return;
  fetch("data/sources.json").then(function (r) { return r.json(); }).then(function (srcs) {
    srcs.forEach(function (s) {
      var d = document.createElement("div"); d.className = "card scans";
      var h = document.createElement("h3"); h.textContent = s.citation; d.appendChild(h);
      if (s.pages.length) { var p = document.createElement("p"); p.textContent = "Printed page(s): " + s.pages.join(", "); d.appendChild(p); }
      if (!s.scans.length) { var f = document.createElement("p"); f.className = "flag"; f.textContent = "⚠ " + (s.flag || "Missing image"); d.appendChild(f); }
      s.scans.forEach(function (src) {
        var a = document.createElement("a"); a.href = src;
        var img = document.createElement("img"); img.src = src; img.loading = "lazy"; img.alt = s.citation + " scan";
        a.appendChild(img); d.appendChild(a);
      });
      box.appendChild(d);
    });
  });
}
document.addEventListener("DOMContentLoaded", function () { initPeople(); initScans(); });

// Jump navigation: collapse on small screens and highlight the section in view.
// Menu dropdowns: tap/keyboard toggle with aria-expanded. Without JS, links and hover still work.
document.addEventListener("DOMContentLoaded", function () {
  var toc = document.querySelector(".toc");
  if (toc) {
    var d = toc.querySelector("details");
    if (d && window.matchMedia && window.matchMedia("(max-width:700px)").matches) d.removeAttribute("open");
    var links = {}, targets = [];
    toc.querySelectorAll('a[href^="#"]').forEach(function (a) {
      var id = a.getAttribute("href").slice(1), el = document.getElementById(id);
      if (el && id !== "top") { links[id] = a; targets.push(el); }
    });
    if ("IntersectionObserver" in window && targets.length) {
      var io = new IntersectionObserver(function (es) {
        es.forEach(function (e) {
          if (!e.isIntersecting) return;
          Object.keys(links).forEach(function (k) { links[k].removeAttribute("aria-current"); });
          var a = links[e.target.id]; if (a) { a.setAttribute("aria-current", "true"); if (a.scrollIntoView && window.innerWidth > 700) a.parentNode.parentNode.scrollLeft = a.offsetLeft - 40; }
        });
      }, { rootMargin: "0px 0px -70% 0px" });
      targets.forEach(function (t) { io.observe(t); });
    }
  }
  // Touch screens (iPhone etc.) have no real hover, so the menu is opened only by this
  // handler: first tap opens, a second tap on the same trigger closes, outside tap/Escape closes.
  // The CSS hover/focus opening is limited to hover-capable devices so a tap can't open the menu
  // mid-gesture and shift the layout under the finger.
  var touch = window.matchMedia && window.matchMedia("(hover: none)").matches;
  function closeAll(except) {
    document.querySelectorAll("nav .dropdown.open").forEach(function (o) {
      if (o === except) return;
      o.classList.remove("open"); o.firstElementChild.setAttribute("aria-expanded", "false");
    });
  }
  function setOpen(li, on) {
    li.classList.toggle("open", on); if (on) li.classList.remove("closed"); li.firstElementChild.setAttribute("aria-expanded", on ? "true" : "false");
  }
  document.querySelectorAll("nav .dropdown > a").forEach(function (a) {
    var li = a.parentNode;
    a.addEventListener("click", function (ev) {
      if (!touch) return;
      ev.preventDefault();
      closeAll(li);
      setOpen(li, !li.classList.contains("open"));
    });
    a.addEventListener("keydown", function (ev) {
      if (ev.key === "ArrowDown" || ev.key === " ") { ev.preventDefault(); closeAll(li); setOpen(li, true); var f = li.querySelector("ul a"); if (f) f.focus(); }
    });
  });
  document.addEventListener("keydown", function (ev) {
    if (ev.key !== "Escape") return;
    var li = document.activeElement && document.activeElement.closest && document.activeElement.closest("nav .dropdown");
    closeAll();
    if (li) { li.classList.add("closed"); li.firstElementChild.focus(); }
  });
  document.querySelectorAll("nav .dropdown").forEach(function (li) {
    li.addEventListener("mouseleave", function () { li.classList.remove("closed"); });
    li.addEventListener("focusout", function (ev) { if (!li.contains(ev.relatedTarget)) li.classList.remove("closed"); });
  });
  document.addEventListener("click", function (ev) {
    if (!ev.target.closest || ev.target.closest("nav .dropdown")) return;
    closeAll();
  });
});

// Long-page section folds: open the target section for #hash links (including
// nested anchors and jump-nav clicks), and wire Expand all / Collapse all.
document.addEventListener("DOMContentLoaded", function () {
  var folds = Array.prototype.slice.call(document.querySelectorAll("details.sec-fold"));
  if (!folds.length) return;

  function openForTarget(el) {
    if (!el) return;
    var node = el;
    while (node) {
      if (node.tagName === "DETAILS" && node.classList && node.classList.contains("sec-fold")) {
        node.open = true;
      }
      node = node.parentElement;
    }
  }

  function revealAndScroll(el) {
    if (!el) return;
    openForTarget(el);
    var root = document.documentElement;
    function jump() {
      // Instant jump so a late layout or the browser's own hash scroll cannot
      // leave the target mid-animation or at its pre-open position.
      root.style.scrollBehavior = "auto";
      if (el.scrollIntoView) el.scrollIntoView();
      root.style.scrollBehavior = "";
    }
    jump();
    requestAnimationFrame(function () {
      requestAnimationFrame(jump);
    });
  }

  function openForHash() {
    var id = (location.hash || "").replace(/^#/, "");
    if (!id) return;
    revealAndScroll(document.getElementById(id));
  }

  window.addEventListener("hashchange", openForHash);
  window.addEventListener("load", openForHash);
  openForHash();

  document.querySelectorAll('.toc a[href^="#"], .to-top a[href^="#"]').forEach(function (a) {
    a.addEventListener("click", function (ev) {
      var href = a.getAttribute("href") || "";
      if (href.charAt(0) !== "#") return;
      ev.preventDefault();
      var id = href.slice(1);
      if (history.replaceState) history.replaceState(null, "", href);
      else location.hash = href;
      revealAndScroll(document.getElementById(id));
    });
  });

  var expand = document.querySelector(".sec-fold-expand");
  var collapse = document.querySelector(".sec-fold-collapse");
  if (expand) expand.addEventListener("click", function () {
    folds.forEach(function (d) { d.open = true; });
  });
  if (collapse) collapse.addEventListener("click", function () {
    folds.forEach(function (d) {
      d.open = d.classList.contains("sec-fold-intro");
    });
  });

  window.addEventListener("beforeprint", function () {
    folds.forEach(function (d) {
      d.dataset.wasOpen = d.open ? "1" : "0";
      d.open = true;
    });
  });
  window.addEventListener("afterprint", function () {
    folds.forEach(function (d) {
      if (d.dataset.wasOpen === "0") d.open = false;
    });
  });
});

// Open letter transcriptions when printing so the text is on the page.
document.addEventListener("DOMContentLoaded", function () {
  var letters = Array.prototype.slice.call(document.querySelectorAll("details.letter-transcript"));
  if (!letters.length) return;
  window.addEventListener("beforeprint", function () {
    letters.forEach(function (d) {
      d.dataset.wasOpen = d.open ? "1" : "0";
      d.open = true;
    });
  });
  window.addEventListener("afterprint", function () {
    letters.forEach(function (d) {
      if (d.dataset.wasOpen === "0") d.open = false;
    });
  });
});
