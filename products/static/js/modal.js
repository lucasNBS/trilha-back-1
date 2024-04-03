const background = document.querySelector("#background")
const modal = document.querySelector("#modal")

background.addEventListener("click", () => {
  window.location.href = '/'
})

modal.addEventListener("click", (e) => {
  e.stopPropagation()
})

const hidden = document.querySelector('#hidden')
const add = document.querySelector('.add')
const remove = document.querySelector('.remove')

add.addEventListener("click", (e) => {
  hidden.value = e.target.innerText
})

remove.addEventListener("click", (e) => {
  hidden.value = e.target.innerText
})
