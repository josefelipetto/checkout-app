<template>
  <div class="container">
    <main>
      <div class="py-5 text-center">
        <h2>Confirm your order</h2>
        <p class="lead">
          Confirm your order and fill payment info. Don't worry, we'll start right after that :)
        </p>
      </div>

      <div class="row g-5">
        <CartItems/>
        <PaymentForm/>
      </div>
    </main>
  </div>
</template>

<script>
import PaymentForm from '@/components/PaymentForm'
import CartItems from '@/components/CartItems'

export default {
  name: 'Checkout',
  components: {
    PaymentForm,
    CartItems
  }
}
</script>

<style scoped>

</style>
