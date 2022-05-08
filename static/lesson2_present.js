//fill dynamically when data is filled
$(document).ready(() => {
    
    
   
   let lesson_name = lesson_params["lesson_name"]
   let description = lesson_params["description"]
   let mushroom1 = lesson_params["mushroom1"] 
    
    


    if (mushroom1["edible"]){
        document.getElementById("banner").style.backgroundColor = "#96D365";
        document.getElementById("banner").innerHTML = "Edible"
    }
    else{
        document.getElementById("banner").style.backgroundColor = "#F68780";
        document.getElementById("banner").innerHTML = "Poisonous"
    }

    document.getElementById("name1").innerHTML = mushroom1["name"]

    document.getElementById("img1").src = mushroom1["img_url"]

    document.getElementById("img2").src = mushroom1["cut_img_url"]

    document.getElementById("cap1").innerHTML = mushroom1["cap"]

    document.getElementById("stem1").innerHTML = mushroom1["stem"]

    document.getElementById("gills1").innerHTML = mushroom1["gills"]

    document.getElementById("color1").innerHTML = mushroom1["color"]

    document.getElementById("inner1").innerHTML = mushroom1["inner"]

    document.getElementById("description").innerHTML = mushroom1["description"]
    
    
    if (lesson_params["next"] == 100){
        document.getElementById("nextButton").innerHTML = "Play Game!"
    }
    
    if ("mushroom2" in lesson_params) {
        document.getElementById("compButton").innerHTML = "Compare to " + lesson_params["mushroom2"]["name"];
        let compare = '"/lesson_compare/' + mushroom1["id"] +  '/' + lesson_params["mushroom2"]["id"] + '"'
        document.getElementById("compButton").setAttribute('onclick','window.location.href = ' + compare)

        
    }
    else{
        var comp = document.getElementById('compButton');
        comp.parentNode.removeChild(comp);
    }
    
    

  })
