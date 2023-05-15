<script>
import Header from '../components/Header.vue'
import OrderForm from '../components/OrderForm.vue'

export default {
  props:['basket', 'deleteBasket'],
  components: { Header, OrderForm }
}
</script>

<template>
  <div>
    <Header :basket="basket" />
    <OrderForm :basket="basket" :deleteBasket="deleteBasket"/>
  </div>
</template>
