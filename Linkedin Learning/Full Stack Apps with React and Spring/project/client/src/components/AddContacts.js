import React, { Component } from 'react';

export default class AddContacts extends Component {
     submitContact(event) {
          event.preventDefault();

          let contact = {
               firstName: this.refs.firstName.nodeValue,
               lastName: this.refs.lastName.value,
               email: this.refs.email.value,
          }

          fetch("http://localhost:8080/api/contacts", {
               method: "POST",
               headers: {
                    "content-type": "application/json",
               },
               body: JSON.stringify(contact),
          })
          .then(response => response.json());

          window.location.reload();
     }
     
     render() {
          return(
               <div classNameName="row">
                    <form classNameName="col s12" onSubmit={this.submitContact.bind(this)}>
                         <div className="row">
                              <div className="input-field col s6">
                                   <input placeholder="Placeholder" id="first_name" type="text" className="validate" />
                                   <label htmlFor="first_name">First Name</label>
                              </div>
                              <div className="input-field col s6">
                                   <input id="last_name" type="text" className="validate" />
                                   <label htmlFor="last_name">Last Name</label>
                              </div>
                         </div>
                         <div className="row">
                         <div className="input-field col s12">
                              <input id="email" type="email" className="validate" />
                              <label htmlFor="email">Email</label>
                         </div>
                         </div>
                         <div className="row">
                              <button classNameName="waves-effect waves-light btn" type="submit" name="action">Submit</button>
                         </div>
                    </form>
             </div>
          )
     }

}