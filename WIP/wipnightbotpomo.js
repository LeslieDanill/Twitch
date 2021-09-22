$(1) $(2) 1 2 3 4 5 6 

edit !pomoset 1 1 $(eval if(`$(1)`!=`null`){`$(1)`}else{`25`}) $(eval if(`$(2)`!=`null`){`$(2)`}else{`5`}) $(time UTC "hh") $(time UTC "mm")

pomo is on a break for x more minutes
pomo is focusing on TASK until 00:00
``

$(eval if($(time UTC "a")='am'){$(time UTC "HH")}else{$(time UTC "HH")+12}) $(eval Math.ceil($(time UTC "mm")))	


@$(channel) is $(eval let messages=["a-ok","irritated","wrathful","furious","in a fit of rage"],hrs=(Date.now()-new Date("$(twitch $(channel) "{{uptimeAt}}")").getTime())/3600000,toIndex=(d,l,u,c)=>d<l?0:d>=u?c-1:Math.floor((c-2)*(d-l)/(u-l))+1;messages[toIndex(hrs,1,5,5)])

$(user) has used the $(eval responses = ["Italian Game", "English Opening", "Sicilian Defence", "Bongcloud Attack", "Fool’s Gambit", "Halloween Gambit", "Ware Opening", "French Defence", "Ruy-Lopez", "Damiano’s Defence", "Alekhine’s Defence"]; responses[Math.floor(Math.random() * responses.length)]) :wink: $(eval responses = ["to win against", "but lost to"]; responses[Math.floor(Math.random() * responses.length)]) :wink: $(urlfetch http://2g.be/twitch/randomviewer.php?channel=$(channel))

add !pomotimer -ul=moderator -cd=5 $(eval if($(time UTC "a")='am'){h=$(time UTC "HH")}else{h=$(time UTC "HH")+12};m=(Math.ceil($(time UTC "mm")/5)*5);(h*60+m)) $(eval String.raw`if($(eval `$`+`(3)`)='am'){nh=$(1)}else{nh=$(1)+12};nm=(Math.ceil($(2)/5)*5);(nh*60+nm)-`)

add !pomotimer -ul=moderator -cd=5 $(eval String.raw`if($(eval `$`+`(3)`)='am'){nh=$(eval `$`+`(1)`)}else{nh=$(eval `$`+`(1)`)+12};nm=(Math.ceil($(eval `$`+`(2)`)/5)*5);(nh*60+nm)-`)$(eval if($(time UTC "a")='am'){h=$(time UTC "HH")}else{h=$(time UTC "HH")+12};m=(Math.ceil($(time UTC "mm")/5)*5);a=h*60+m)

add !pomotimer -ul=moderator -cd=5 $(eval String.raw`$(eval `$`+`(eval `)if($(eval `$`+`(3)`)='am'){h=$(eval `$`+`(1)`)}else{h=$(eval `$`+`(1)`)+12};m=(Math.ceil($(eval `$`+`(2)`)/5)*5);h*60+nm-`)$(eval if($(time UTC "a")='am'){h=$(time UTC "HH")}else{h=$(time UTC "HH")+12};m=(Math.ceil($(time UTC "mm")/5)*5);a=h*60+m))

$(eval String.raw`if($(eval `$`+`(3)`)='am'){h=$(eval `$`+`(1)`)}else{h=$(eval `$`+`(1)`)+12};m=(Math.ceil($(eval `$`+`(2)`)/5)*5);h*60+m-`)$(eval if($(time UTC "a")='am'){h=$(time UTC "HH")}else{h=$(time UTC "HH")+12};m=(Math.ceil($(time UTC "mm")/5)*5);a=h*60+m)