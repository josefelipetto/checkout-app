<template>
  <main>
    <div id="main-content" v-if="isApiConnected">
      <MarketingCall title="Order now :)" text="Choose a meal, place an order and let the magic begins."/>
      <ul class="nav nav-tabs justify-content-center" id="myTab" role="tablist">
        <li class="nav-item" role="presentation" v-for="(category, idx) in categories" :key="idx">
          <button :class="'nav-link ' + (idx === 0 ? ' active ' : '') "
                  :id="toTabName(category.name) + '-tab'"
                  data-bs-toggle="tab"
                  :data-bs-target="'#' + toTabName(category.name)"
                  type="button"
                  role="tab"
                  :aria-controls="toTabName(category.name)"
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
              :id="toTabName(category.name)" role="tabpanel"
              :aria-labelledby="toTabName(category.name) + '-tab'"
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
    </div>
    <ErrorMessage v-if="!isApiConnected"
                  title="Whoops :("
                  text="We're really sorry. It looks like we're having connectivity issues. Wait a few moments and try again. "
                  :reload-button="true"
    />
  </main>
</template>

<script>
import MarketingCall from '@/components/layout/MarketingCall'
import ItemCard from '@/components/items/ItemCard'
import ErrorMessage from '@/components/helpers/ErrorMessage'

const headers = { Accept: 'application/json' }

export default {
  name: 'Home',
  components: {
    MarketingCall,
    ItemCard,
    ErrorMessage
  },
  data: () => ({
    categories: [],
    items: [],
    isApiConnected: true
  }),
  methods: {
    itemsByCategory (categoryId) {
      return this.items.filter(item => item.category_id === categoryId)
    },
    toTabName: name => name.replace(' ', '_').toLowerCase(),
    setCategories () {
      fetch(this.baseAPIUrl + '/menu/category', { headers })
        .then(response => response.json())
        .then(categories => {
          this.categories = categories
          this.isApiConnected = true
        })
        .catch(_ => {
          this.isApiConnected = false
        })
    },
    setItems () {
      fetch(this.baseAPIUrl + '/menu/product', { headers })
        .then(response => response.json())
        .then(items => {
          this.items = items
          this.isApiConnected = true
        })
        .catch(_ => {
          this.isApiConnected = false
        })
    }
  },
  beforeMount () {
    this.setCategories()
    this.setItems()
  }
}
</script>
