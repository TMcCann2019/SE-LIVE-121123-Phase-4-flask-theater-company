import React, {useState} from 'react'
import {useHistory} from 'react-router-dom'
import styled from "styled-components";
import { useFormik } from "formik"
import * as yup from "yup"


function Authentication({updateUser}) {
  const [signUp, setSignUp] = useState(false)
  const history = useHistory()

  const handleClick = () => setSignUp((signUp) => !signUp)
  // 3.✅ Finish building the authentication form with formik
    // 3.1 create a formSchema and use yup to make some client side validations
    // 3.2 Use formik to handle the value, onchange and onsubmit of the form
    // 3.3 on submit create a POST. 
      // 3.4 There is a button that toggles the component between login and sign up.
      // if signUp is true use the path '/users' else use '/login' (we will be writing login soon)
      // Complete the post and test our '/users' route 
    // 3.4 On a successful POST add the user to state (updateUser is passed down from app through props) and redirect to the Home page.
  // 4.✅ return to server/app.py to build the next route

    const formSchema = yup.object.shape({
      name: yup.string().required("Please enter your name"),
      email: yup.string().email("Please enter a valid email")
    })

    const formik = useFormik({
      initialValues: {
        name : "",
        email : ""
      },
      validationSchema: formSchema,
      onSubmit: (values) => {
        fetch(signUp ? '/singup' : '/login', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(values, null, 2),
        })
        .then((res) => {
          if (res.ok){
            res.json().then(user => {
              updateUser(user)
              history.push('/')
            })
          } else {
            updateUser(null)
            history.push('/authentication')
          }
        })
      }
    })
 
    return (
        <> 
        {formik.errors && Object.values(formik.errors).map((error) => <h2 style = {{color: 'red'}}> {error}</h2>)}
        <h2>Please Log in or Sign up!</h2>
        <h2>{signUp?'Already a member?':'Not a member?'}</h2>
        <button onClick={handleClick}>{signUp?'Log In!':'Register now!'}</button>
        <Form onSubmit={formik.handleSubmit}>
        <label>
          Username
          </label>
        <input type='text' name='name' value={'value'} onChange={formik.handleChange} />
        {signUp&&(
          <>
          <label>
          Email
          </label>
          <input type='text' name='email' value={'value'} onChange={formik.handleChange} />
          </>
        )}
        <input type='submit' value={signUp?'Sign Up!':'Log In!'} />
      </Form>
        </>
    )
}

export default Authentication

export const Form = styled.form`
display:flex;
flex-direction:column;
width: 400px;
margin:auto;
font-family:Arial;
font-size:30px;
input[type=submit]{
  background-color:#42ddf5;
  color: white;
  height:40px;
  font-family:Arial;
  font-size:30px;
  margin-top:10px;
  margin-bottom:10px;
}
`