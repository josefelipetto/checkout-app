import { createStore } from 'vuex'
import createPersistedState from 'vuex-persistedstate'

export default createStore({
  state: {
    /**
     * The cart.
     */
    cart: {},
    /**
     * The number of items on the cart
     */
    cartTotalItems: 0
  },
  mutations: {
    /**
     * Add an item to the cart
     * @param state
     * @param product
     */
    addCartItem (state, product) {
      if (product.id in state.cart) {
        state.cart[product.id].quantity++
      } else {
        state.cart[product.id] = {
          ...product,
          quantity: 1
        }
      }
      state.cartTotalItems++
    },
    /**
     * remove an unity of an item from the cart
     * @param state
     * @param productId
     */
    removeCartItem (state, productId) {
      if (state.cartTotalItems <= 0) {
        return
      }

      if (!(productId in state.cart)) {
        return
      }

      if (state.cart[productId].quantity > 0) {
        state.cart[productId].quantity--
        state.cartTotalItems--
      }
    },
    /**
     * Delete the item from the cart
     * @param state
     * @param productId
     */
    deleteCartItem (state, productId) {
      if (state.cartTotalItems <= 0) {
        return
      }

      if (!(productId in state.cart)) {
        return
      }

      const itemQuantity = state.cart[productId].quantity
      delete state.cart[productId]
      state.cartTotalItems -= itemQuantity
    },
    /**
     * Empty the cart
     * @param state
     * @param payload
     */
    emptyCart (state, payload) {
      state.cart = {}
      state.cartTotalItems = 0
    }
  },
  actions: {
  },
  modules: {},
  getters: {
    /**
     * Get current cart
     * @param state
     * @return {{}}
     */
    getCart: state => state.cart,
    /**
     * Get current number of items on the cart
     * @param state
     * @return {number}
     */
    getCartTotalItems: state => state.cartTotalItems,
    /**
     * Get the total spent so far on the cart
     * @param state
     * @return {number}
     */
    getCartTotalSpent: state => {
      const cartIterator = Object.keys(state.cart)
      return cartIterator.reduce((acc, productId) => {
        const totalItemPrice = (state.cart[productId].quantity * state.cart[productId].price)
        return acc + totalItemPrice
      }, 0)
    }
  },
  plugins: [
    /**
     * Plugin to persist cart and cartTotalItems on local storage to
     * avoid losing state after refreshing and/or closing the tab
     */
    createPersistedState({
      paths: ['cart', 'cartTotalItems']
    })
  ]
})
