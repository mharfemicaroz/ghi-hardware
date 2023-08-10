<template>
    <div class="calculator-set">
        <div class="calculatortotal">
            <h4>0</h4>
        </div>
        <ul>
            <li v-for="number in numbers">
                <a href="javascript:void(0);" @click=""></a>
            </li>
            <li>
                <a href="javascript:void(0);" class="btn btn-closes" @click=""><img src="/img/icons/close-circle.svg" alt="img"></a>
            </li>
            <li>
                <a href="javascript:void(0);" class="btn btn-reverse" @click=""><img src="/img/icons/reverse.svg" alt="img"></a>
            </li>
        </ul>
    </div>
</template>
<script>

export default {
    data() {
        return {

        };
    },
    methods: {

    },
}

</script>
<style></style>