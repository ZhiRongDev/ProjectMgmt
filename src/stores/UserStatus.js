import axios from 'axios'
import { defineStore } from 'pinia'

export default defineStore('UserStatus', {
    // 等於 data
    state: () => {
        return {
            User: {
                User_ID: '',
                User_Name: '',
                User_Mail: '',
                User_Avatar: '',
                User_Password: ''
            },
        }
    },
    // 等於 computed
    getters: {},
    // 等於 methods
    actions: {
    }
})
