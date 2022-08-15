// "use strict";

// document.addEventListener("DOMContentLoaded", function () {
//     // Modals

//     var rootEl = document.documentElement;
//     var $modals = getAll(".modal");
//     var $modalButtons = getAll(".modal-button");
//     var $modalCloses = getAll(
//         ".modal-background, .modal-close, .modal-card-head .delete, .modal-card-foot .button"
//     );

//     if ($modalButtons.length > 0) {
//         $modalButtons.forEach(function ($el) {
//             $el.addEventListener("click", function () {
//                 var target = $el.dataset.target;
//                 openModal(target);
//             });
//         });
//     }

//     if ($modalCloses.length > 0) {
//         $modalCloses.forEach(function ($el) {
//             $el.addEventListener("click", function () {
//                 closeModals();
//             });
//         });
//     }

//     function openModal(target) {
//         var $target = document.getElementById(target);
//         rootEl.classList.add("is-clipped");
//         $target.classList.add("is-active");
//     }

//     function closeModals() {
//         rootEl.classList.remove("is-clipped");
//         $modals.forEach(function ($el) {
//             $el.classList.remove("is-active");
//         });
//     }

//     document.addEventListener("keydown", function (event) {
//         var e = event || window.event;

//         if (e.keyCode === 27) {
//             closeModals();
//             closeDropdowns();
//         }
//     });

//     // Utils

//     function getAll(selector) {
//         var parent =
//             arguments.length > 1 && arguments[1] !== undefined
//                 ? arguments[1]
//                 : document;

//         return Array.prototype.slice.call(parent.querySelectorAll(selector), 0);
//     }
// });

!(function () {
    var t, n, e, o, l, c, a, d, i, m, u;
    function s(e, t) {
        document.querySelectorAll(e).forEach(function (e) {
            e.addEventListener("click", t);
        });
    }
    ((t = "data-target"),
    (n = "is-active"),
    (e = ".modal-button"),
    (o = ".modal-close"),
    (l = ".modal-button-close"),
    (c = ".modal-background"),
    (a = function () {
        document.querySelectorAll("." + n).forEach(function (e) {
            e.classList.remove(n);
        }),
            u();
    }),
    (d = function () {
        var e = this.getAttribute(t);
        m(), document.getElementById(e).classList.add(n);
    }),
    (i = function () {
        var e = this.parentElement.id;
        document.getElementById(e).classList.remove(n), u();
    }),
    (m = function () {
        (document.getElementsByTagName("html")[0].style.overflow = "hidden"),
            (document.getElementsByTagName("body")[0].style.overflowY =
                "scroll");
    }),
    (u = function () {
        (document.getElementsByTagName("html")[0].style.overflow = ""),
            (document.getElementsByTagName("body")[0].style.overflowY = "");
    }),
    {
        init: function () {
            s(e, d),
                s(o, i),
                s(l, a),
                s(c, i),
                document.addEventListener("keyup", function (e) {
                    27 == e.keyCode && a();
                });
        },
    }).init();
})();
