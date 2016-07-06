var gulp = require('gulp');
var sass = require('gulp-sass');
var watch = require('gulp-watch');
var minifycss = require('gulp-minify-css');
var rename = require('gulp-rename');
var gzip = require('gulp-gzip');
var livereload = require('gulp-livereload');
var merge = require('merge-stream');
var symlink = require('gulp-sym');
var fs = require('fs');

var js_folders = ['bower_components/foundation/js/foundation/'];

var gzip_options = {
    threshold: '1kb',
    gzipOptions: {
        level: 9
    }
};

/* Compile Our Sass */
gulp.task('sass', function() {
    return gulp.src('scss/*.scss')
        .pipe(sass())
        .pipe(gulp.dest('aquaman/static/stylesheets'))
        .pipe(rename({suffix: '.min'}))
        .pipe(minifycss())
        .pipe(gulp.dest('aquaman/static/stylesheets'))
        .pipe(gzip(gzip_options))
        .pipe(gulp.dest('aquaman/static/stylesheets'))
        .pipe(livereload());
});



// gulp.task('js', function () {
//     if (!fs.existsSync('aquaman/static/bower_components/')) {
//         gulp.src('bower_components/*')
//             .pipe(symlink('aquaman/static/bower_components/')) // Write to the destination folder
//     }
// });

/* Move font files */
gulp.task('fonts', function(){
    return gulp.src('bower_components/components-font-awesome/fonts/*')
        .pipe(gulp.dest('aquaman/static/fonts/'))
});

/* Watch Files For Changes */
gulp.task('watch', function() {
    livereload.listen();
    gulp.watch('scss/**/*.scss', ['sass']);

    /* Trigger a live reload on any Django template changes */
    gulp.watch('**/templates/*').on('change', livereload.changed);

});

gulp.task('default', ['sass', 'fonts', 'watch']);
