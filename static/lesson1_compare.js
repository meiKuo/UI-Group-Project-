//fill dynamically when data is filled
$(document).ready(() => {
    let lesson_name = lesson_params["lesson_name"]
    let description = lesson_params["description"]
    let mushroom1 = lesson_params["mushroom1"]
    let mushroom2 = lesson_params["mushroom2"]

    document.getElementById("name1").innerHTML = mushroom1["name"]
    document.getElementById("name2").innerHTML = mushroom2["name"]
    
    document.getElementById("img1").src = mushroom1["img_url"]
    document.getElementById("img2").src = mushroom2["img_url"]
    
    document.getElementById("edible1").innerHTML = mushroom1["edible"]
    document.getElementById("edible2").innerHTML = mushroom2["edible"]
    
    document.getElementById("cap1").innerHTML = mushroom1["cap"]
    document.getElementById("cap2").innerHTML = mushroom2["cap"]
    
    document.getElementById("stem1").innerHTML = mushroom1["stem"]
    document.getElementById("stem2").innerHTML = mushroom2["stem"]
    
    document.getElementById("gills1").innerHTML = mushroom1["gills"]
    document.getElementById("gills2").innerHTML = mushroom2["gills"]
    
    document.getElementById("taste1").innerHTML = mushroom1["taste"]
    document.getElementById("taste2").innerHTML = mushroom2["taste"]
    
    document.getElementById("color1").innerHTML = mushroom1["color"]
    document.getElementById("color2").innerHTML = mushroom2["color"]
    
    document.getElementById("location1").innerHTML = mushroom1["location"]
    document.getElementById("location2").innerHTML = mushroom2["location"]
    
    document.getElementById("inner1").innerHTML = mushroom1["inner"]
    document.getElementById("inner2").innerHTML = mushroom2["inner"]
    

  
  })
