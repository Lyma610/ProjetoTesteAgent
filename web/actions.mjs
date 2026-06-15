export function bindSubmit(button, handler) {
  button.addEventListener("click", handler);
}

export function nextCounter(current) {
  return current + 1;
}
