<template>
  <main>
    <MarketingCall title="Order now :)" text="Choose a meal, place an order and let the magic begins."/>

    <ul class="nav nav-tabs justify-content-center" id="myTab" role="tablist">
      <li class="nav-item" role="presentation" v-for="(category, idx) in categories" :key="idx">
        <button :class="'nav-link ' + (idx === 0 ? ' active ' : '') "
                :id="category.name + '-tab'"
                data-bs-toggle="tab"
                :data-bs-target="'#' + category.name"
                type="button"
                role="tab"
                :aria-controls="category.name"
                aria-selected="true">
          {{ category.name }}
        </button>
      </li>
    </ul>
    <div class="py-5 bg-light">
      <div class="container">
        <div class="tab-content" id="myTabContent">
          <div
            v-for="(category, idx) in categories" :key="idx"
            :class="'tab-pane fade show' + (idx === 0 ? ' active ' : '')"
            :id="category.name" role="tabpanel"
            :aria-labelledby="category.name + '-tab'"
          >
            <div class="row row-cols-1 row-cols-sm-2 row-cols-md-3 g-3">
              <div class="col" v-for="(product, index) in itemsByCategory(category.id)" :key="index">
                <ItemCard :category="category" :product="product"/>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </main>
</template>

<script>
import MarketingCall from '@/components/layout/MarketingCall'
import ItemCard from '@/components/items/ItemCard'

export default {
  name: 'Home',
  components: {
    MarketingCall,
    ItemCard
  },
  methods: {
    itemsByCategory (categoryId) {
      return this.items.filter(item => item.category_id === categoryId)
    }
  },
  computed: {
    categories () {
      return this.$store.getters.getCategories
    },
    items () {
      return this.$store.getters.getItems
    }
  }
}
</script>
