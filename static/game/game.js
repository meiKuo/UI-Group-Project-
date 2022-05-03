const GAME_STATE = {
    Start: 0,
    Map: 1,
    OnChoice: 2,
    OnEatConfirm: 3,
    OnCut: 4,
    OnToxicConfirm: 5,
    Continue: 6,
}

const BUTTON_COLOR = {
    Red: "button-red",
    Green: "button-green",
    Gray: "button-gray",
}

function setDialogue(dialogue) {
    $(".dialogue-box").text(dialogue)
}

function createGameButton(text, color, nextState) {
    return `<button data-next=${nextState} class="game-button ${color}">${text}</button>`

}

function updateButtons(buttons) {
    $(".button-box").empty()
    $.each(buttons, function (_, button) {
        const { text, color, nextState } = button
        $(".button-box").append($(createGameButton(text, color, nextState)))
    })
}

function updateState() {
    console.log(gameState)
    switch (gameState) {
        case (GAME_STATE.Start):
            updateButtons([
                {
                    text: "Play",
                    color: BUTTON_COLOR.Green,
                    nextState: GAME_STATE.Map
                }
            ])
            break;
        case (GAME_STATE.Map):
            $(".button-box").empty()
            break;
        case (GAME_STATE.OnChoice):
            setDialogue("Hmm, this looks interesting. What will you do?")
            updateButtons([
                {
                    text: "Let's eat it!",
                    color: BUTTON_COLOR.Green,
                    nextState: GAME_STATE.OnEatConfirm,
                },
                {
                    text: "Hmm, cut it open.",
                    color: BUTTON_COLOR.Gray,
                    nextState: GAME_STATE.OnCut
                },
                {
                    text: "Nah, it's toxic!",
                    color: BUTTON_COLOR.Red,
                    nextState: GAME_STATE.OnToxicConfirm
                },
            ])
            break;
        case (GAME_STATE.OnEatConfirm):
            setDialogue("Are you sure you want to eat this?")
            updateButtons([
                {
                    text: "Yes, let's eat it!",
                    color: BUTTON_COLOR.Green,
                    nextState: GAME_STATE.Continue
                },
                {
                    text: "No, go back.",
                    color: BUTTON_COLOR.Gray,
                    nextState: GAME_STATE.OnChoice
                }
            ])
            break;
        case (GAME_STATE.OnToxicConfirm):
            setDialogue("Are you sure this mushroom is toxic?")
            updateButtons([
                {
                    text: "Not sure, go back.",
                    color: BUTTON_COLOR.Gray,
                    nextState: GAME_STATE.OnChoice
                },
                {
                    text: "Yes, stay away!",
                    color: BUTTON_COLOR.Red,
                    nextState: GAME_STATE.Continue
                },
            ])
            break;
        case (GAME_STATE.OnCut):
            updateButtons([
                {
                    text: "Back",
                    color: BUTTON_COLOR.Gray,
                    nextState: GAME_STATE.OnChoice,
                }
            ])
            break;
        case (GAME_STATE.Continue):
            updateButtons([
                {
                    text:"Continue",
                    color: BUTTON_COLOR.Green,
                    nextState: GAME_STATE.Map,
                }
            ])
            break;
        default:
            console.log("Error: Invalid state.")
    }
}

function onUserChoiceResult(result) {
    const { health, hunger, mushroomName, eat, edible } = result;

    if (eat) {
        if (edible) {
            setDialogue(`Congrats! You just ate a ${mushroomName}. It was edible!`)
        } else {
            setDialogue(`Uh oh! You just ate a ${mushroomName}. It was toxic. You will lose some health!`)
        }
    } else {
        if (edible) {
            setDialogue(`Oh no! That was a ${mushroomName}. It was edible, so you will gain some health`)
        } else {
            setDialogue(`Great! That was a ${mushroomName}. It was super toxic, so it's good to avoid it!`)
        }
    }

    $(".health-bar").css("width", `${health}%`)
    $(".health-bar").text(health)

    gameState = GAME_STATE.Continue;
    updateState()
}

function submitData(data) {
    $.ajax({
        type: "POST",
        url: "/update",
        dataType : "json",
        contentType: "application/json; charset=utf-8",
        data : JSON.stringify(data),
        success: function(result) {
            onUserChoiceResult(result)
        },
        error: function(request, status, error){
            console.log("Error");
            console.log(request)
            console.log(status)
            console.log(error)
        }
    });
}

function submitUserChoice() {
    if (gameState == GAME_STATE.OnEatConfirm)
        submitData({
            eat: true,
            quiz_id: quiz
        })
    else if (gameState == GAME_STATE.OnToxicConfirm)
        submitData({
            eat: false,
            quiz_id: quiz
        })
}

function onGameButtonPress(nextState) {
    switch (nextState) {
        case (GAME_STATE.Start):
            return;
        case (GAME_STATE.Map):
            window.location.href = '/game/map'
            return;
        case (GAME_STATE.Continue):
            submitUserChoice()
            return;
    }

    gameState = nextState
    updateState()
}

$(document).ready(() => {
    updateState()

    $(document).on("click", ".game-button", function() {
        onGameButtonPress($(this).data("next"))
    })
})
