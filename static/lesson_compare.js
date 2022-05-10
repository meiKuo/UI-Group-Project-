$(document).ready(() => {
    let mushroom1 = lesson_params["mushroom1"]
    let mushroom2 = lesson_params["mushroom2"]
    
    if (mushroom1["edible"]){
        document.getElementById("banner1").style.backgroundColor = "#96D365";
        document.getElementById("banner1").innerHTML = "Edible"
    }
    else{
        document.getElementById("banner1").style.backgroundColor = "#F68780";
        document.getElementById("banner1").innerHTML = "Toxic"
    }
    
    if (mushroom2["edible"]){
        document.getElementById("banner2").style.backgroundColor = "#96D365";
        document.getElementById("banner2").innerHTML = "Edible"
    }
    else{
        document.getElementById("banner2").style.backgroundColor = "#F68780";
        document.getElementById("banner2").innerHTML = "Toxic"
    }
    
    
    document.getElementById("img1").src = mushroom1["img_url"]

    document.getElementById("img2").src = mushroom2["img_url"]
    
    
    document.getElementById("cap1").innerHTML = mushroom1["cap"]
    
    document.getElementById("cap2").innerHTML = mushroom2["cap"]
    
    document.getElementById("stem1").innerHTML = mushroom1["stem"]
    
    document.getElementById("stem2").innerHTML = mushroom2["stem"]
    
    document.getElementById("gills1").innerHTML = mushroom1["gills"]
    
    document.getElementById("gills2").innerHTML = mushroom2["gills"]
    
    document.getElementById("color1").innerHTML = mushroom1["color"]
    
    document.getElementById("color2").innerHTML = mushroom2["color"]
    
    document.getElementById("inner1").innerHTML = mushroom1["inner"]
    
    document.getElementById("inner2").innerHTML = mushroom2["inner"]
    
  })
