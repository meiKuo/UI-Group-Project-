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
    $(".button_row").empty()
    if (idx == 0){
      $("#dialog").text("Are you sure you don't want to eat the mushroom?")
      $(".button_row").append($(
          `<button id="backButton" class="noEatButton">No, I'm not sure.</button>
          <button id="toMapButton" class="eatButton">Stay Away. Back to Map</button>`
      ))
    }
    else if (idx == 1){
      $("#dialog").text("Always good to be cautious. What should we do to help us decide?")
      $(".button_row").append($(
          `<button id="backButton" class="noEatButton">Back</button>
          <button id="cutButton">Let's cut it open</button>
          <button id="guidebookButton">Let's refer to the mushroom guidebook!</button>`
      ))
    }
    else if (idx == 2){
      $("#dialog").text("Are you sure it's safe to eat?")
      $(".button_row").append($(
          `<button id="backButton" class="noEatButton">No, I'm not sure.</button>
          <button id="finalEatButton" class="eatButton">Yes, let's eat it</button>`
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

function choiceMade(choice, mushroom){
  if (choice == 'eat'){
    $("#dialog").text("You just ate a " + mushroom['name'] + " mushroom!")
    setTimeout(
      function(){
        if (mushroom['edible']){
          $("#dialog").text("Congratulations! It was an edible mushroom :)")
          setTimeout(function(){
            console.log('changing screens now')
            choicePostReq(choice, mushroom);
          }, 2500);
        }
        else{
          $("#dialog").text("Unfortunately it was poisonous so you lost 10 health :(")
          setTimeout(function(){
            console.log('changing screens now')
            choicePostReq(choice, mushroom);
          }, 3000);
        }
      }, 2500);

  }
  else {
    choicePostReq(choice, mushroom)
  }
}

function choicePostReq(choice, mushroom){
  console.log('choicePostReq', choice, mushroom)
  let data = {
    "choice": choice,
    "mushroom": mushroom
  }

  $.ajax({
      type: "POST",
      url: "/update",
      dataType : "json",
      contentType: "application/json; charset=utf-8",
      data : JSON.stringify(data),
      success: function(result){
          console.log('result', result);
          window.location.href = "/game/map"
      },
      error: function(request, status, error){
          console.log("Error");
          console.log('request', request)
          console.log('status', status)
          console.log('error', error)
      }
  });
}

$(document).ready(function(){
    // resetChoices()

    $("#dialog").text("Hmm this mushroom looks interesting. What should we do with it?")

    // $(document).on("click", ".game-button", function() {
    //     const idx = $(this).data("idx")
    //     if (idx !== undefined){
    //         submitUserAnswer(idx)
    //     }
    // })
    $("#noEatButton").click(function(){
        updateOnAnswer(0)
    })
    $(document).on("click", "#noEatButton", function() {
        updateOnAnswer(0)
    })

    $("#notSureButton").click(function(){
        updateOnAnswer(1)
    })
    $(document).on("click", "#notSureButton", function() {
        updateOnAnswer(1)
    })

    $("#eatButton").click(function(){
        updateOnAnswer(2)
    })
    $(document).on("click", "#eatButton", function() {
        updateOnAnswer(2)
    })

    $(document).on("click", "#toMapButton", function() {
        choiceMade("notEat", mushroom);
    })
    $(document).on("click", "#finalEatButton", function() {
        choiceMade("eat", mushroom);
    })

    $(document).on("click", "#backButton", function() {
        $(".button_row").empty()
        $("#dialog").text("Hmm this mushroom looks interesting. What should we do with it?")
        $(".button_row").append($(
            `<button id="noEatButton" class="noEatButton">This looks dangerous. Let's stay away.</button>
            <button id="notSureButton" class="notSureButton">Hmm, not sure</button>
            <button id="eatButton" class="eatButton">Looks edible! Let's eat it!</button>`
        ))
    })


    //
    // $(document).on("click", "#eatButton2", function() {
    //     window.location.href = "/game/1"
    // })

    //
    // $(document).on("click", "#cutButton", function() {
    //     window.location.href = "/game/1"
    // })


})
