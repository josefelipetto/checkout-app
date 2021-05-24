import { createStore } from 'vuex'
import createPersistedState from 'vuex-persistedstate'

export default createStore({
  state: {
    cart: {},
    cartTotalItems: 0,
    categories: [
      {
        id: 1,
        image_id: 'f3fbf57b118fa9',
        name: 'Bakery'
      },
      {
        id: 2,
        image_id: 'b271afbefdc554',
        name: 'Entrees'
      },
      {
        id: 3,
        image_id: 'eba73b2361fae3',
        name: 'Drinks'
      }],
    items: [
      {
        category_id: 1,
        id: 1,
        image_id: '293202f9d9f7f4',
        name: 'Bagel',
        price: 2.0
      },
      {
        category_id: 1,
        id: 2,
        image_id: '808916fd5ddf96',
        name: 'Croissant',
        price: 1.0
      },
      {
        category_id: 1,
        id: 3,
        image_id: '95d02a230fe050',
        name: 'Muffin',
        price: 1.25
      },
      {
        category_id: 1,
        id: 4,
        image_id: '23f95765b967ff',
        name: 'Toast / Bread',
        price: 1
      },
      {
        category_id: 1,
        id: 5,
        image_id: '5650be5d48a99b',
        name: 'English Muffin',
        price: 2.5
      },
      {
        category_id: 2,
        id: 6,
        image_id: 'bd237a0c0d19ef',
        name: 'Pasta Bar',
        price: 12.99
      },
      {
        category_id: 2,
        id: 7,
        image_id: '3e1bd1342800f7',
        name: 'Mediterranean Entree',
        price: 10.99
      },
      {
        category_id: 2,
        id: 8,
        image_id: '72589c4c990f97',
        name: 'Indian Entree',
        price: 11.95
      },
      {
        category_id: 3,
        id: 9,
        image_id: '70c2a6247e7b58',
        name: 'Small Drink',
        price: 0.75
      },
      {
        category_id: 3,
        id: 10,
        image_id: 'dba0fc03da30ca',
        name: 'Medium Drink',
        price: 1.5
      },
      {
        category_id: 3,
        id: 11,
        image_id: 'ffc9bf61e441cd',
        name: 'Large Drink',
        price: 2
      }
    ]
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
