<template>
  <div>
    <input ref="upfile" type="file" v-on:change="imageToBase64"/><br/><br/>
    <img  class="inline object-center " v-if="showPrev" v-bind:src="previewBase64" alt="preview" width="300"/><br/><br/>
    <button v-if="showUpload" class="btn btn-primary" v-on:click="upload">upload</button>
    <br/>
    <br/>
    <p v-if="showOutput">出力結果 : {{smRetvalue}}</p>  
  </div>
</template>

<script>
import axios from 'axios'
import {reactive} from 'vue'

const smRequests = reactive({
  Image: ''
})

//const rootname = "http://ec2-52-194-191-241.ap-northeast-1.compute.amazonaws.com"
const rootname = "http://localhost"

export default {
  name: 'FileUp',
  data(){
    return {
      showPrev: false,
      showUpload: false,
      showOutput: false,
      previewBase64: '',
      smRetvalue:'unkown'
    }
  },
  methods: {
    imageToBase64(event){
      const reader = new FileReader()

      // 選択されたファイルの取得
      const file = event.target.files[0]

      // ファイルが選択されていればBase64に変換する
      if(file){
        reader.readAsDataURL(file)
      }else{
        this.previewBase64 = ''
      }

      // 変換が終わったら実行される
      reader.onload = () => {
        this.showPrev = true
        this.showUpload = true
        this.previewBase64 = reader.result
      }
    },

    upload() {
      const endPoint = rootname + ':5000/api/sm'
      //console.log(this.smRetvalue)
      smRequests.Image = this.previewBase64
      axios.post(endPoint,smRequests).then( 
        (response) => {
          this.smRetvalue = response.data.result
          this.showOutput = true
        }
      ).catch( (error) => {
        console.log(error)
      })
    }
  },

}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
