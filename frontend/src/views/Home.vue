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
                <ItemCard :category="category" :product="product" />
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </main>
</template>

<script>
import MarketingCall from '@/components/MarketingCall'
import ItemCard from '@/components/ItemCard'

export default {
  name: 'Home',
  components: {
    MarketingCall,
    ItemCard
  },
  data: function () {
    return {
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
        }
      ],
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
    }
  },
  methods: {
    itemsByCategory (categoryId) {
      return this.items.filter(item => item.category_id === categoryId)
    }
  }
}
</script>
