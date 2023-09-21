// || Initialize Modules
const { src, dest, watch, series } = require("gulp");
const autoprefixer = require("autoprefixer");
const cssnano = require("cssnano");
const babel = require("gulp-babel");
const concat = require("gulp-concat");
const postcss = require("gulp-postcss");
const rename = require("gulp-rename");
const sourcemaps = require("gulp-sourcemaps");
const terser = require("gulp-terser");
const exec = require("child_process").exec;

// CSS Task
function cssTask() {
  var proc = exec(
    "npx tailwindcss -i ./assets/css/main.css -o ./static/css/main.min.css --watch"
  );
  return new Promise(function (resolve, reject) {
    resolve();
  });
}

// |  CSS Build Task
function cssBuildTask() {
  return src("static/css/main.min.css")
    .pipe(sourcemaps.init({ loadMaps: true }))
    .pipe(postcss([autoprefixer(), cssnano()]))
    .pipe(sourcemaps.write(".", { addComment: false }))
    .pipe(dest("static/css"));
}

// |  JavaScript Task
function jsTask() {
  return src("assets/js/**/*.js")
    .pipe(concat("main.js"))
    .pipe(sourcemaps.init({ loadMaps: true }))
    .pipe(rename({ suffix: ".min" }))
    .pipe(sourcemaps.write(".", { addComment: false }))
    .pipe(dest("static/js"));
}

// |  JavaScript Build Task
function jsBuildTask() {
  return src("assets/js/**/*.js")
    .pipe(concat("main.js"))
    .pipe(sourcemaps.init({ loadMaps: true }))
    .pipe(babel({ presets: ["@babel/preset-env"] }))
    .pipe(terser())
    .pipe(rename({ suffix: ".min" }))
    .pipe(sourcemaps.write(".", { addComment: false }))
    .pipe(dest("static/js"));
}

// |  Watch Task
function watchTask() {
  watch("assets/js/**/*.js", jsTask);
}

// ||  Gulp Tasks
exports.default = series(cssTask, jsTask, watchTask); // gulp
exports.build = series(cssBuildTask, jsBuildTask); // gulp build

// |  Functions
exports.css = cssTask; // gulp css
exports.cssBuild = cssBuildTask; // gulp cssBuild
exports.js = jsTask; // gulp js
exports.jsBuild = jsBuildTask; // gulp jsBuild
