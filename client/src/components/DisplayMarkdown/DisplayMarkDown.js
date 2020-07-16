import React, { Component } from 'react';
import ReactMarkdown from 'react-markdown';
import './DisplayMarkdown.css'

class DisplayMarkdown extends Component {
    constructor(props) {
        super(props);
        this.state = {
            body: `# Markdown Editor\n\`code block\`\n\n## Subheader\n`,
            title: 'Sample'
        };

        // this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }
    
    // handleChange(event) {
    //     const target = event.target;
    //     const name = target.name;
    //     const value = name.value;

    //     this.setState({
    //         ...this.state,
    //         [name]: value
    //     });
    //     // console.log(this.state)
    // }

    handleChange = (name) => (event) => {
        const updatedState = {
            ...this.state,
            [name]: event.target.value
        }
        this.setState(updatedState)
    }

    handleSubmit(event) {
        event.preventDefault();
        let url = '/create';
        // let formData = new FormData();
        let data = this.state;

        fetch(url, {
            method: 'POST',
            body: JSON.stringify(data),
            headers: { 'Content-Type': 'application/json' }
        })
        .then((res) => {
            return res.json()
        })
        .catch(error => {
            console.log(error) 
        })
    }

    render() {
        return (
            <div className='DisplayMarkdown'>
                <div className="row">
                    <div className="inner-header">
                        <h1>Editor</h1>
                    </div>
                    <div className="inner-header">
                        <h1>Preview</h1>
                    </div>
                </div>
                <form onSubmit={this.handleSubmit}>
                    <div className="row long">
                    <div className="editor">
                        <input 
                            name='title'
                            type='text' 
                            value={this.state.title} 
                            onChange={this.handleChange('title')} />

                        <textarea 
                            name='body'
                            value={this.state.body} onChange={this.handleChange('body')} />
                    </div>
                    <div className="preview">
                        <ReactMarkdown  
                            source={this.state.body}
                            />
                    </div>
                    </div>
                    <div className="row save-button">
                    <input 
                        type="submit" 
                        value="save"
                    />
                    </div>
                </form>
            </div>
        );
    }
}

export default DisplayMarkdown;