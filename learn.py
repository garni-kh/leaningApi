#!/usr/bin/python
# -*- coding: <utf-8> -*-
import os, sys
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash, request,jsonify
from datetime import timedelta
from datetime import datetime
from flask import abort, redirect, url_for
from datetime import date
import datetime

from learning import testa




@app.route("/_autocomplate/<text>", methods=['post', 'GET'])
@login_required
def _autocomplate(text=None):
    a = text
    print(a)
    #a1=red.lrange("words1", 0, -1)
   # for i in a1:
    #    print(i.decode("utf-8"))
    # SSCAN words2 0 MATCH e* COUNT 10000
    text1 = red.sscan("words22", "0", "%s*"%(a) , count="11000")
    res=[]
    for i in text1:
        print(i)
        if isinstance(i, int) is True:
           res.append(i)
        else:

            for f in i:
                res.append(f.decode("utf-8"))
    alo = res[1:]
    print("-------------")

    print(alo)
   
    return jsonify(resultING=alo)


@app.route("/_autocomplateDIP/<text>", methods=['post', 'GET'])
@login_required
def _autocomplateDIP(text): 
  # text must be an 40 len of world or  space decorate in js site  
        print("-------last -40--in root- >>> 40 ---")
        a1=text
        print(len(a1))
        if len(a1) <= 39 :
          a2 = " "*(40-len(a1))+a1
          print("this is the len of cochak %s"%len(a2))
          print("and this is after decoreitthin conent::: %s"%(a2))
          b=yad.testa(a2)
          return jsonify(resultDIP=b)
        else :

         b=yad.testa(a1)
         return jsonify(resultDIP=b)
