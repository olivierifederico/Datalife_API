
  H = (function () {
    function t(t, e) {
        var i = t.scale,
            s = t.values;
        (this._scale = i), (this._values = s), (this._fromColor = this.hexToRgb(i[0])), (this._toColor = this.hexToRgb(i[1])), (this._map = e), this.setMinMaxValues(s), this.visualize();
    }
    var e = t.prototype;
    return (
        (e.setMinMaxValues = function (t) {
            for (var e in ((this.min = Number.MAX_VALUE), (this.max = 0), t)) (e = parseFloat(t[e])) > this.max && (this.max = e), e < this.min && (this.min = e);
        }),
        (e.visualize = function () {
            var t,
                e = {};
            for (var i in this._values) (t = parseFloat(this._values[i])), isNaN(t) || (e[i] = this.getValue(t));
            this.setAttributes(e);
        }),
        (e.setAttributes = function (t) {
            for (var e in t) this._map.regions[e] && this._map.regions[e].element.setStyle("fill", t[e]);
        }),
        (e.getValue = function (t) {
            for (var e, i = "#", s = 0; s < 3; s++) i += (1 === (e = Math.round(this._fromColor[s] + (this._toColor[s] - this._fromColor[s]) * ((t - this.min) / (this.max - this.min))).toString(16)).length ? "0" : "") + e;
            return i;
        }),
        (e.hexToRgb = function (t) {
            var e = 0,
                i = 0,
                s = 0;
            return (
                4 == t.length ? ((e = "0x" + t[1] + t[1]), (i = "0x" + t[2] + t[2]), (s = "0x" + t[3] + t[3])) : 7 == t.length && ((e = "0x" + t[1] + t[2]), (i = "0x" + t[3] + t[4]), (s = "0x" + t[5] + t[6])),
                [parseInt(e), parseInt(i), parseInt(s)]
            );
        }),
        t
    );
})(),

map.extend("hibrido", function (newParams) {
    this.reset();
    
    // Remove old regions from DOM then empty the object
    Object.keys(this.regions).forEach((key) => {
        const el = this.regions[key].element.shape.node;
        el.parentElement.removeChild(el);
    });
    this.regions = {};
    
    // Overwrite the old params with the new params
    Object.keys(newParams).forEach((key) => {
        this.params[key] = newParams[key];
    });
    
    this._createRegions();
    this.updateSize();
    this._createMarkers(this.params.markers);
    this._repositionLabels();
    this._setupElementEvents()
    // "jvm-series-container jvm-series-h"
    // "jvm-series-container jvm-series-v"
    this.params.visualizeData && (this.dataVisualization = new H(this.params.visualizeData, this))
    const legendHorizontal = document.createElement("div");
    const legendVertical = document.createElement("div");
    
    legendHorizontal.setAttribute("class", "jvm-series-h");
    legendVertical.setAttribute("class", "jvm-series-v");
    
    this.legendHorizontal = legendHorizontal;
    this.legendVertical = legendVertical;
    
    if (this.params.series) {
        this.container.appendChild(this.legendHorizontal);
        this.container.appendChild(this.legendVertical);
        this._createSeries();
    }
    });