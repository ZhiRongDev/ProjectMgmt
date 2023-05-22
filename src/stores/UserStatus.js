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
            },
        }
    },
    // 等於 computed
    getters: {},
    // 等於 methods
    actions: {
        logout() {
            localStorage.removeItem('User')
            this.router.replace('/')
        },
        load_UserInfo() {
            const UserInfo = JSON.parse(localStorage.getItem('User'))
            this.User.User_ID = UserInfo.User_ID;
            this.User.User_Name = UserInfo.User_Name;
            this.User.User_Mail = UserInfo.User_Mail;
            this.User.User_Avatar = UserInfo.User_Avatar;
        },
        checkAuth() {
            if (
                !localStorage.getItem('User') ||
                localStorage.getItem('User').User_ID === null
            ) {
                this.logout()
            } else {
                this.load_UserInfo()
            }
        },
    }
})
