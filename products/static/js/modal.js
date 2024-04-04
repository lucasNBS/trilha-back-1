const buttons = document.querySelectorAll(".modal")
const modalFrame = document.querySelector("#modal-frame")

buttons.forEach(button => {
  button.addEventListener("click", (e) => {
    modalFrame.classList.remove('disapear')
    background.classList.remove('disapear')
    
    const type = e.target.dataset.type.toLowerCase()
    modalFrame.src = `products/${e.target.dataset.id}/${type}`
  })
})

const background = document.querySelector("#background")

background.addEventListener("click", () => {
  modalFrame.classList.add('disapear')
  background.classList.add('disapear')
})

modalFrame.addEventListener("click", (e) => {
  e.stopPropagation()
})
