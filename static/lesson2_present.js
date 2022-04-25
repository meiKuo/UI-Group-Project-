//fill dynamically when data is filled
$(document).ready(() => {
    let lesson_name = lesson_params["lesson_name"]
    let description = lesson_params["description"]
    let mushroom1 = lesson_params["mushroom1"]

    $("#backButton").click(function(){
      window.location.href ='/lessonplans'
    })

    document.getElementById("name1").innerHTML = mushroom1["name"]

    document.getElementById("img1").src = mushroom1["img_url"]

    document.getElementById("edible1").innerHTML = mushroom1["edible"]

    document.getElementById("cap1").innerHTML = mushroom1["cap"]

    document.getElementById("stem1").innerHTML = mushroom1["stem"]

    document.getElementById("gills1").innerHTML = mushroom1["gills"]

    document.getElementById("taste1").innerHTML = mushroom1["taste"]

    document.getElementById("color1").innerHTML = mushroom1["color"]

    document.getElementById("location1").innerHTML = mushroom1["location"]

    document.getElementById("inner1").innerHTML = mushroom1["inner"]

    document.getElementById("description").innerHTML = mushroom1["description"]


  })
