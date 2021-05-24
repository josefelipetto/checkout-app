import { createStore } from 'vuex'
import createPersistedState from 'vuex-persistedstate'

const URL = 'http://localhost:5000/'
const headers = { Accept: 'application/json' }
export default createStore({
  state: {
    cart: {},
    cartTotalItems: 0,
    categories: [],
    items: []
  },
  mutations: {
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
    setItems (state, payload) {
      state.items = payload
    },
    setCategories (state, payload) {
      state.categories = payload
    },
    emptyCart (state, payload) {
      state.cart = {}
      state.cartTotalItems = 0
    }
  },
  actions: {
    async setCategories (state) {
      const categories = (await fetch(URL + 'menu/category', { headers })).json()
      state.commit('setCategories', categories)
    },
    async setItems (state) {
      const products = (await fetch(URL + 'menu/product', { headers })).json()
      state.commit('setItems', products)
    }
  },
  modules: {},
  getters: {
    getCart: state => state.cart,
    getCartTotalItems: state => state.cartTotalItems,
    getCategories: state => state.categories,
    getItems: state => state.items,
    getCartTotalSpent: state => {
      const cartIterator = Object.keys(state.cart)
      return cartIterator.reduce((acc, productId) => {
        const totalItemPrice = (state.cart[productId].quantity * state.cart[productId].price)
        return acc + totalItemPrice
      }, 0)
    }
  },
  plugins: [
    createPersistedState()
  ]
})
