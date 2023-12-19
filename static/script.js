#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 21:33:24 2023

@author: simonmeyer
"""
document.addEventListener("DOMContentLoaded", function() {
    var footer = document.getElementById("dynamic-footer");
    var lastScrollTop = 0;

    window.addEventListener("scroll", function() {
        var st = window.pageYOffset || document.documentElement.scrollTop;
        
        if (st > lastScrollTop) {
            // Scrolling down, hide the footer
            footer.style.display = "none";
        } else {
            // Scrolling up, show the footer
            footer.style.display = "block";
        }

        lastScrollTop = st;
    });
});
