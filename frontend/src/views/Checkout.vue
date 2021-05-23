<template>
  <div class="container">
    <main>
      <MarketingCall
        title="Confirm your order"
        text="Confirm your order and fill payment info. Don't worry, we'll start right after that :)"
      />
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
import MarketingCall from '@/components/MarketingCall'

export default {
  name: 'Checkout',
  components: {
    PaymentForm,
    CartItems,
    MarketingCall
  }
}
</script>

<style scoped>

</style>
