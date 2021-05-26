<template>
  <Header />
  <router-view />
  <Footer />
</template>

<script>
import Header from '@/components/layout/Header.vue'
import Footer from '@/components/layout/Footer.vue'
/**
 * App component
 * @displayName App Component
 */
export default {
  name: 'app',
  components: {
    Header,
    Footer
  }
}
</script>
