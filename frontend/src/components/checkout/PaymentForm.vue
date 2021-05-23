<template>
  <OrderResultModal ref="resultModal"/>

  <div class="col-md-7 col-lg-8">
    <div class="alert alert-danger" role="alert" v-if="errors.length">
      <ul>
        <li v-for="(error,idx) in errors" :key="idx">{{ error }}</li>
      </ul>
    </div>
    <h4 class="mb-3">Personal information</h4>
    <form class="needs-validation" novalidate="">
      <div class="row g-3">
        <div class="col-sm-6">
          <label for="firstName" class="form-label">First name</label>
          <input
            type="text"
            class="form-control"
            id="firstName"
            v-model="firstName"
          >
          <div class="invalid-feedback">
            Valid first name is required.
          </div>
        </div>
        <div class="col-sm-6">
          <label for="lastName" class="form-label">Last name</label>
          <input
            type="text"
            class="form-control"
            id="lastName"
            v-model="lastName"
          >
          <div class="invalid-feedback">
            Valid last name is required.
          </div>
        </div>
        <div class="col-12">
          <label for="email" class="form-label">Email <span class="text-muted">(Optional)</span></label>
          <input
            type="email"
            class="form-control"
            id="email"
            placeholder="you@example.com"
            v-model="email"
          >
          <div class="invalid-feedback">
            Please enter a valid email address for shipping updates.
          </div>
        </div>
      </div>
      <hr class="my-4">
      <h4 class="mb-3">Payment information</h4>
      <div class="my-3">
        <div class="form-check">
          <input
            id="credit"
            name="paymentMethod"
            type="radio"
            class="form-check-input"
            v-model="paymentMethod"
          >
          <label class="form-check-label" for="credit">Credit card</label>
        </div>
        <div class="form-check">
          <input
            id="debit"
            name="paymentMethod"
            type="radio"
            class="form-check-input"
            v-model="paymentMethod"
          >
          <label class="form-check-label" for="debit">Debit card</label>
        </div>
        <div class="form-check">
          <input
            id="paypal"
            name="paymentMethod"
            type="radio"
            class="form-check-input"
            v-model="paymentMethod"
          >
          <label class="form-check-label" for="paypal">PayPal</label>
        </div>
      </div>

      <div class="row gy-3">
        <div class="col-md-6">
          <label for="cc-name" class="form-label">Name on card</label>
          <input
            type="text"
            class="form-control"
            id="cc-name"
            v-model="ccName"
          >
          <small class="text-muted">Full name as displayed on card</small>
          <div class="invalid-feedback">
            Name on card is required
          </div>
        </div>

        <div class="col-md-6">
          <label for="cc-number" class="form-label">Credit card number</label>
          <input
            type="text"
            class="form-control"
            id="cc-number"
            v-model="ccNumber"
          >
          <div class="invalid-feedback">
            Credit card number is required
          </div>
        </div>

        <div class="col-md-3">
          <label for="cc-expiration" class="form-label">Expiration</label>
          <input
            type="text"
            class="form-control"
            id="cc-expiration"
            v-model="ccExpiration"
          >
          <div class="invalid-feedback">
            Expiration date required
          </div>
        </div>

        <div class="col-md-3">
          <label for="cc-cvv" class="form-label">CVV</label>
          <input
            type="text"
            class="form-control"
            id="cc-cvv"
            v-model="ccCVV"
          >
          <div class="invalid-feedback">
            Security code required
          </div>
        </div>
      </div>

      <hr class="my-4">

      <button
        class="w-100 btn btn-primary btn-lg"
        @click="pay"
        type="button"
        :disabled="cartTotalItems <= 0"
      >
        {{ checkoutButtonLabel }}
      </button>
    </form>
  </div>
</template>

<script>
import OrderResultModal from '@/components/checkout/OrderResultModal'

export default {
  name: 'PaymentForm',
  data: () => ({
    errors: [],
    firstName: null,
    lastName: null,
    email: null,
    paymentMethod: null,
    ccName: null,
    ccNumber: null,
    ccExpiration: null,
    ccCVV: null
  }),
  methods: {
    pay () {
      if (!this.validateForm()) {
        return
      }
      const success = true
      this.$refs.resultModal.setType(success === true ? 'S' : 'F')
      this.$refs.resultModal.show()
    },
    validateForm () {
      this.errors = []

      let hasErrors = false

      if (!this.firstName) {
        this.errors.push('First name should be provided.')
        hasErrors = true
      }

      if (!this.lastName) {
        this.errors.push('Last name should be provided.')
        hasErrors = true
      }

      if (!this.email) {
        this.errors.push('Email must be provided.')
        hasErrors = true
      } else if (!this.validEmail(this.email)) {
        this.errors.push('Valid email required.')
        hasErrors = true
      }

      if (!this.paymentMethod) {
        this.errors.push('Payment method must be provided.')
        hasErrors = true
      }

      if (!this.ccName) {
        this.errors.push('Name on card must be provided.')
        hasErrors = true
      }

      if (!this.ccNumber) {
        this.errors.push('Card Number must be provided.')
        hasErrors = true
      }

      if (!this.ccExpiration) {
        this.errors.push('Card Expiration must be provided.')
        hasErrors = true
      }

      if (!this.ccCVV) {
        this.errors.push('Card CVV must be provided.')
        hasErrors = true
      }

      return !hasErrors
    },
    validEmail: function (email) {
      const re = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
      return re.test(email)
    }
  },
  computed: {
    cartTotalItems () {
      return this.$store.getters.getCartTotalItems
    },
    checkoutButtonLabel () {
      return this.cartTotalItems <= 0 ? 'Add some items to proceed' : 'Proceed to Checkout'
    }
  },
  components: {
    OrderResultModal
  }
}
</script>
