import axios from 'axios'
import { defineStore } from 'pinia'

export default defineStore('ProjectStatus', {
    // 等於 data
    state: () => {
        return {
            Project: {
                Project_ID: '',
                Project_Name: '',
            },
        }
    },
    // 等於 computed
    getters: {},
    // 等於 methods
    actions: {
    }
})
