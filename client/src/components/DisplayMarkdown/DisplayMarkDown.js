import React, { Component } from 'react';
import ReactMarkdown from 'react-markdown';
import './DisplayMarkdown.css'

class DisplayMarkdown extends Component {
    constructor(props) {
        super(props);
        this.state = {
            value: `# Markdown Editor\n\`code block\`\n\n## Subheader\n`
        };

        this.handleChange = this.handleChange.bind(this);
    }
    
    handleChange(event) {
        this.setState({value: event.target.value});
    }

    render() {
        return (
            <div>

                <div className="container">
                    <div className="inner-header">
                        <h1>Editor</h1>
                    </div>
                    <div className="inner-header">
                        <h1>Preview</h1>
                    </div>
                </div>
                <div class="container">
                    <div className="editor">
                        <textarea value={this.state.value} onChange={this.handleChange}/>
                    </div>
                    <div className="preview">
                        <ReactMarkdown 
                            source={this.state.value}
                        />
                    </div>
                </div>

            </div>
        );
    }
}

export default DisplayMarkdown;