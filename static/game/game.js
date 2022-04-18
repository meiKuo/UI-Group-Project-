function submitUserAnswer(idx) {
    $.ajax({
        type: "POST",
        url: "/update",
        dataType : "json",
        contentType: "application/json; charset=utf-8",
        data : JSON.stringify(idx),
        success: function(result) {
            console.log(result)
            updateLives(result["lives"])
            updateOnAnswer(idx)
        },
        error: function(request, status, error){
            console.log("Error");
            console.log(request)
            console.log(status)
            console.log(error)
        }
    });
}

function updateLives(nLives) {
    $("#heart-container").empty()
    for (let i = 0; i < nLives; i++) {
        $("#heart-container").append($(
            `<img src='/static/game/assets/heart.png' />`
        ))
    }
}

function updateHunger(){

}

function updateOnAnswer(idx) {
    // $("#dialogue").text(question.choices[idx].dialogue)
    console.log('idx', idx);
    $(".button-box").empty()
    if (idx == 0){
      $("#dialogue").text("No problem, let's move on to another mushroom.")
      $(".button-box").append($(
          `<button id="toMapButton">Back to map</button>`
      ))
    }
    else if (idx == 1){
      $("#dialogue").text("Always good to be cautious. What should we do to help us decide?")
      $(".button-box").append($(
          `<button id="cutButton">Let's cut it open</button>
          <button id="guidebookButton">Let's refer to the mushroom guidebook!</button>`
      ))
    }
    else if (idx == 2){
      $("#dialogue").text("Are you sure it's safe to eat?")
      $(".button-box").append($(
          `<button id="noEatButton2" class="noEatButton">No, I'm not sure.</button>
          <button id="eatButton2" class="eatButton">Yes, let's eat it</button>`
      ))
    }

}


function resetChoices() {
    $.each(question.choices, (i, val) => {
        $(".button-box").append($(
            `<a type="button" class="game-button" data-idx=${i}>${val.text}</a>`
        ))
    })
}

$(document).ready(() => {
    resetChoices()

    $(document).on("click", ".game-button", function() {
        const idx = $(this).data("idx")
        if (idx !== undefined){
            submitUserAnswer(idx)
        }
    })
    $("#noEatButton").click(function(){
        updateOnAnswer(0)
    })
    $("#notSureButton").click(function(){
        updateOnAnswer(1)
    })
    $("#eatButton").click(function(){
        updateOnAnswer(2)
    })

    $("#toMapButton").click(function(){
        console.log('back to map')
    })

    $(document).on("click", "#noEatButton2", function() {
        window.location.href = "/game/1"
    })

    $(document).on("click", "#eatButton2", function() {
        window.location.href = "/game/1"
    })

    $(document).on("click", "#toMapButton", function() {
        window.location.href = "/game/1"
    })

    $(document).on("click", "#cutButton", function() {
        window.location.href = "/game/1"
    })


})
