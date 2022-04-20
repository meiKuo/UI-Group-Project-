$(document).ready(() => {
  console.log('data', data['health'])
  let health = data['health']
  if (health > 0) {
    $('#end_game_title').text('Congratulations! You survived the wild wild wilderness!')
    $('#end_game_sub').text('Your final score is: ' + health + '/100')
  }
  else {
    $('#end_game_title').text('GAME OVER!')
    $('#end_game_sub').text('You made some very poor decisions along the way and unfortunately lost all your health :(')
  }

})
