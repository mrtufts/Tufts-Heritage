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
