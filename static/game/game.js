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

function updateOnAnswer(idx) {
    // $("#dialogue").text(question.choices[idx].dialogue)
    console.log('idx', idx);
    $(".button-box").empty()
    if (idx == 0){
      $(".button-box").append($(
          `<a type="button" class="game-button" href="/game/">Continue</a>`
      ))
    }
    else if (idx == 1){
      $(".button-box").append($(
          `<a type="button" class="game-button" href="/game/">Let's cut it open</a>
          <a type="button" class="game-button" href="/game/">Let's refer to the mushroom guidebook!</a>`
      ))
    }
    else if (idx == 2){
      $(".button-box").append($(
          `<button id="eatButton2" class="eatButton">Yes, let's eat it</button>
          <button id="noEatButton2" class="noEatButton">No, I'm not sure.</button>`
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

    $("#eatButton2").click(function(){
        updateOnAnswer(2)
    })
    $("#noEatButton2").click(function(){
      console.log('2 pressed')
        // window.location.href = "https://www.google.com";
    })
})
