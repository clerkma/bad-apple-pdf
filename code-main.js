// https://opensource.adobe.com/dc-acrobat-sdk-docs/library/jsapiref/JS_API_AcroJS.html
var w = globalThis.getField("console");
var t = 0;
var i = null;
var dots = "\u2026";
var dash = "\u2014";

function progress(index) {
    var n = (index / 6574) * 78;
    return "\n\n\n\nProgress => \n" + dots.repeat(n) + dash.repeat(78 - n);
}

function play() {
    if (t < 6575) {
        w.value = "\n\n\n\n\n\n\n\n" + frame[t % 6574] + progress(t);
        t += 1;
    } else {
        if (i != null) {
            app.clearInterval(i);
            i = null;
        }
        t = 0;
        w.value = "";
    }
}

// 30 fps
function start() {
    if (i == null) {
        i = app.setInterval("play()", 33);
    }
}
