const modalFrame = document.querySelector("#modal")

const hidden = document.querySelector('#hidden')
const add = document.querySelector('.add')
const remove = document.querySelector('.remove')

add.addEventListener("click", (e) => {
  hidden.value = e.target.innerText
})

remove.addEventListener("click", (e) => {
  hidden.value = e.target.innerText
})

modalFrame.addEventListener("submit", (e) => {
  window.close()
})
