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
                <div class="food-card">
                  <div class="food-card_img">
                    <img src="https://i.imgur.com/eFWRUuR.jpg" :alt="product.image_id">
                    <a href="#!"><i class="far fa-heart"></i></a>
                  </div>
                  <div class="food-card_content">
                    <div class="food-card_title-section">
                      <a href="#!" class="food-card_title">{{ product.name }}</a>
                      <a href="#!" class="food-card_author">{{ category.name }}</a>
                    </div>
                    <div class="food-card_bottom-section">
                      <hr>
                      <div class="space-between">
                        <div class="food-card_price">
                          <span>{{ product.price }}$</span>
                        </div>
                        <div class="food-card_order-count">
                          <div class="input-group mb-3">
                            <div class="input-group-prepend">
                              <button class="btn btn-outline-secondary minus-btn"
                                      type="button"
                              >
                                <BIconPlus/>
                              </button>
                            </div>
                            <input type="text" class="form-control input-manulator" placeholder=""
                                   aria-label="Example text with button addon"
                                   value="0">
                            <div class="input-group-append">
                              <button class="btn btn-outline-secondary add-btn"
                                      type="button"
                              >
                                <BIconDash/>
                              </button>
                            </div>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
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
import { BIconPlus, BIconDash } from 'bootstrap-icons-vue'

export default {
  name: 'Home',
  components: {
    MarketingCall,
    BIconPlus,
    BIconDash
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

<style scoped>
.food-card {
  background: #fff;
  border-radius: 5px;
  overflow: hidden;
  margin-bottom: 30px;
  -webkit-box-shadow: 0 2px 10px rgba(0, 0, 0, 0.06);
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.06);
  -webkit-transition: 0.1s;
  transition: 0.1s;
}

.food-card:hover {
  -webkit-box-shadow: 0 5px 20px rgba(0, 0, 0, 0.1);
  box-shadow: 0 5px 20px rgba(0, 0, 0, 0.1);
}

.food-card .food-card_img {
  display: block;
  position: relative;
}

.food-card .food-card_img img {
  width: 100%;
  height: 200px;
  -o-object-fit: cover;
  object-fit: cover;
}

.food-card .food-card_img i {
  position: absolute;
  top: 20px;
  right: 30px;
  color: #fff;
  font-size: 25px;
  -webkit-transition: all 0.1s;
  transition: all 0.1s;
}

.food-card .food-card_img i:hover {
  top: 18px;
  right: 28px;
  font-size: 29px;
}

.food-card .food-card_content {
  padding: 15px;
}

.food-card .food-card_content .food-card_title-section {
  height: 100px;
  overflow: hidden;
}

.food-card .food-card_content .food-card_title-section .food-card_title {
  font-size: 24px;
  color: #333;
  font-weight: 500;
  display: block;
  line-height: 1.3;
  margin-bottom: 8px;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
  text-overflow: ellipsis;
}

.food-card .food-card_content .food-card_title-section .food-card_author {
  font-size: 15px;
  display: block;
}

.food-card .food-card_content .food-card_bottom-section .space-between {
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-pack: justify;
  -ms-flex-pack: justify;
  justify-content: space-between;
}

.food-card .food-card_content .food-card_bottom-section .food-card_subscribers {
  margin-left: 17px;
}

.food-card .food-card_content .food-card_bottom-section .food-card_subscribers img,
.food-card .food-card_content .food-card_bottom-section .food-card_subscribers .food-card_subscribers-count {
  height: 45px;
  width: 45px;
  border-radius: 45px;
  border: 3px solid #fff;
  margin-left: -17px;
  float: left;
  background: #f5f5f5;
}

.food-card .food-card_content .food-card_bottom-section .food-card_subscribers .food-card_subscribers-count {
  position: relative;
}

.food-card .food-card_content .food-card_bottom-section .food-card_subscribers .food-card_subscribers-count span {
  position: absolute;
  top: 50%;
  left: 50%;
  -webkit-transform: translate(-50%, -50%);
  transform: translate(-50%, -50%);
  font-size: 13px;
}

.food-card .food-card_content .food-card_bottom-section .food-card_price {
  font-size: 28px;
  font-weight: 500;
  color: #F47A00;
}

.food-card .food-card_content .food-card_bottom-section .food-card_order-count {
  width: 130px;
}

.food-card .food-card_content .food-card_bottom-section .food-card_order-count input {
  background: #f5f5f5;
  border-color: #f5f5f5;
  -webkit-box-shadow: none;
  box-shadow: none;
  text-align: center;
}

.food-card .food-card_content .food-card_bottom-section .food-card_order-count button {
  border-color: #f5f5f5;
  border-width: 3px;
  -webkit-box-shadow: none;
  box-shadow: none;
}

@media (min-width: 992px) {
  .food-card--vertical {
    display: -webkit-box;
    display: -ms-flexbox;
    display: flex;
    position: relative;
    height: 235px;
  }

  .food-card--vertical .food-card_img img {
    width: 200px;
    height: 100%;
    -o-object-fit: cover;
    object-fit: cover;
  }
}
</style>
