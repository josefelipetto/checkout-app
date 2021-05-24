<template>
  <Header />
  <router-view />
  <Footer />
</template>

<script>
import Header from '@/components/layout/Header.vue'
import Footer from '@/components/layout/Footer.vue'

export default {
  name: 'app',
  mounted () {
    this.$store.dispatch('setCategories')
    this.$store.dispatch('setItems')
  },
  components: {
    Header,
    Footer
  }
}
</script>
