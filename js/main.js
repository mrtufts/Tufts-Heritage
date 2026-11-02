// Project 1776 site script. Asset paths are built from ASSET_BASE_URL (config.js).
function assetUrl(path) {
  return ASSET_BASE_URL.replace(/\/$/, "") + "/" + path.replace(/^\//, "");
}
document.addEventListener("DOMContentLoaded", function () {
  var y = document.getElementById("year");
  if (y) y.textContent = new Date().getFullYear();
});
