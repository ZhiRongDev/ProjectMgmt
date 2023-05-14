import axios from 'axios'
import { defineStore } from 'pinia'

export default defineStore('ProjectStatus', {
    // 等於 data
    state: () => {
        return {
            Project: {
                Project_ID: '',
                Project_Name: '',
                Project_Color: '',
                collaborators: [
                    {
                        User_ID: '',
                        User_Name: '',
                        User_Mail: '',
                        User_Avatar: '',
                        User_Password: ''
                    }
                ],
            },
        }
    },
    // 等於 computed
    getters: {},
    // 等於 methods
    actions: {
    }
})
