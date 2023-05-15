<script>
import axios from 'axios'

export default{
    props:['basket', 'deleteBasket'],
    data(){
        return{
            error:'',
            name:'',
            surname:'',
            email:'',
            phone:''
        }
    },
    computed:{
        getSumma(){
            return this.basket.reduce((total, next) => total + parseFloat(next.price), 0)
        }
    },
    methods:{
        sendData(){
            if(this.name.length < 2)
                this.error = 'Имя не менее 2 символов'
            else if(this.surname.length < 2)
                this.error = 'Фамилия не менее 2 символов'
            else if(!this.email.includes('@') || !this.email.includes('.'))
                this.error = 'Email неверного типа'
            else if(this.phone.length < 2)
                this.error = 'Телефон не менее 2 символов'
            else if(this.basket.length == 0 || this.getSumma == 0)
                this.error = 'Корзина пустая'
            else {
                this.error = ''
                
                const data = {
                    'name' :this.name,
                    'surname' :this.surname,
                    'email' :this.email,
                    'phone' :this.phone,
                    'summa' :this.getSumma,
                    'basket' :JSON.stringify(this.basket)
                }

                axios.post('http://127.0.0.1:8000/api/order-add/', data)
                    .then(res => {
                        this.error = res.data.result
                        
                        setTimeout(() => {
                            location.href=res.data.url
                        }, 1000);
                    })
            }
        }
    }
}
</script>

<template>
   <div> 
    <h1>Оформление заказа</h1>
    <div class="data">  
        <div class="basket" v-if="this.basket.length > 0">         
            <div class="item" v-for ="el in basket" :key="el.slug">
                <img :src="'/img/' + el.image" :alt="el.title">
                <h3>{{ el.title }}</h3>
                <span>{{ el.price }}$</span> 
                <button @click="deleteBasket(el.slug)">Удалить</button>
            </div>
            <span>Итого: {{ getSumma }}$</span>
        </div>
        <div v-else>
            <h2>Товаров нет</h2>
        </div>
        <form>
            <p class="error">{{ error }}</p>
           <input type="text" v-model="name" placeholder="Ваше имя">
           <input type="text" v-model="surname" placeholder="Ваше фамилия">
           <input type="email" v-model="email" placeholder="Ваш email">
           <input type="phone" v-model="phone" placeholder="Ваш номер телефона">
           <button type="button" @click="sendData()">Купить</button>
        </form>
    </div>
    </div>
</template>

<style scoped>
.data{
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin: 50px 0;
}

.data .basket{
    width: 40%;
}
h1{
    text-align: center;
    margin-top: 150px;
    font-size: 90px;
}

.basket .item {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 20px;
}

.basket .item img {
    width: 60px;
}

.basket .item h3 {
    color: #52585c;
    font-size: 15px;
    text-align: center;
}

.basket .item span {
    font-weight: 600;
    color: #323232;
}

 button {
    cursor: pointer;
    border: 0;
    height: 40px;
    background: #e70a0a;
    color: #eef0f1;
    font-weight: 800;
    padding: 7px 12px ;
    font-size: 14px;
    transition: all 500ms ease;
   border-radius: 5px;
}

.basket button:hover {
    background: #640303;
    
}

form input {
    width: 300px;
    padding: 10px 15px;
    border: 1.5px solid #575d61;
    border-radius: 2px;
    background: #81898e;
    margin-bottom: 20px;
    display: block;
    color: #fff;
    outline: none;
    font-size: 15px;
}

form input::placeholder {
    color: rgba(64, 64, 64, 0.531);
}

form input:focus {
    border-color: #242424;
}

form button {
    background: #206E5B;
}

form button:hover {
    background: #134438;
}

.error {
    margin-bottom: 10px;
    color: rgb(181, 46, 46);
}
</style>