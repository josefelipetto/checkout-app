/**
 * Get current page title
 * @param vm
 * @return {*}
 */
function getTitle (vm) {
  const { title } = vm.$options
  if (title) {
    return typeof title === 'function'
      ? title.call(vm)
      : title
  }
}

/**
 * Exports mixin to be used across the system
 */
export default {
  created () {
    const title = getTitle(this)
    if (title) {
      document.title = title
    }
  }
}
