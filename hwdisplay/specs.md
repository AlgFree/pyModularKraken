# specifications


## example config
example hexa.config:


    [main]
    width=1024
    height=600
    load=hexa.py
    destination=ifd
    bg="#000000"
    fg="#ffffff"
    font=("Arial", 25)
    pages=info,audio,desktopcontrol,hidcontrol,obscontrol
    
    [info]
    cpu_description=type:label|text="CPU",x=250,y=50
    cpu_hexa=type:label,image:assets/hexa.png|x=250,y=60
    cpu_percent=type:label,repeatevery:0.5:hexa.cpupercent|x=250,y=80
    
    gpu_description=type:label|text="GPU",x=450,y=50
    gpu_hexa=type:label,image:assets/hexa.png|x=450,y=60
    gpu_percent=type:label,repeatevery:0.5:hexa.gpupercent|x=450,y=80

    ram_description=type:label|text="RAM",x=650,y=50
    ram_hexa=type:label,image:assets/hexa.png|x=650,y=60
    ram_percent=type:label,repeatevery:0.5:hexa.rampercent|x=650,y=80

    nic_description=type:label|text="NIC",x=650,y=50
    nic_hexa=type:label,image:assets/hexa.png|x=650,y=60
    nic_percent=type:label,repeatevery:0.5:hexa.nic|x=650,y=80

    tcpu_description=type:label|text="TEMP_CPU",x=250,y=250
    tcpu_hexa=type:label,image:assets/hexa.png|x=250,y=260
    tcpu=type:label,repeatevery:0.5:hexa.tcpu|x=250,y=280

    tgpu_description=type:label|text="TEMP_GPU",x=450,y=250
    tgpu_hexa=type:label,image:assets/hexa.png|x=450,y=260
    tgpu=type:label,repeatevery:0.5:hexa.tgpu|x=450,y=280

    tsys_description=type:label|text="TEMP_SYS",x=650,y=250
    tsys_hexa=type:label,image:assets/hexa.png|x=650,y=260
    tsys=type:label,repeatevery:0.5:hexa.tsys|x=650,y=280

    [audio]
    notext=type:label|text="Nothing to see here in the audio page",x=250,y=50

    [desktopcontrol]
    notext=type:label|text="Nothing to see here in the desktopcontrol page",x=250,y=50

    [hidcontrol]
    notext=type:label|text="Nothing to see here in the hidcontrol page",x=250,y=50

    [obscontrol]
    notext=type:label|text="Nothing to see here in the obscontrol page",x=250,y=50