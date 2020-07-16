import React from 'react'

// Landing page for people that visit the site
function Landing() {
    return (
        // <div className="landing">
        //     <div></div>

        //     <div></div>

        //     <div></div>

        //     <div></div>
        // </div>

        <div className='landing'>
            <div className="jumbotron jumbotron-fluid jumbotron-bg" style= {
                { 
                    backgroundImage: `url(${process.env.PUBLIC_URL}/image/paper_stack.jpg)`,
                    backgroundSize: 'cover'
                }} >
                <div className="container p-5 jumbo-text">
                    <h1 className="display-4">STAPLE</h1>
                    {/* <hr className="my-4"> */}
                    <p className="lead"> I LIKE FOOD IS POTATOE. NO TOYS ALLOWED.</p>
                    <p className="text-right">
                        <a href="/accounts/login/" className="btn btn-info btn-lg">MAKE A PACKET NOW</a>
                    </p>
                </div>
            </div>

            <div className="container-fluid">
                <div className="card-deck">
                    <div className="card col-sm-4">
                        <i className="far fa-folder fa-5x text-center pt-4"></i>
                        <div className="card-body">
                            <h4 className="card-title text-center">Organize</h4>
                            <p className="card-text"><i>I'm Roxxxy Andrews and I'm here to make it clear,</i> I know you love me, baby,
                                that's why you brought me here. Was a botch on Season 5, I'm gonna make it right; Give me a sewing
                                challenge and I'll give you what you like.</p>
                        </div>
                    </div>
                    <div className="card col-sm-4">
                        <i className="fas fa-clipboard-list fa-5x text-center pt-4"></i>
                        <div className="card-body">
                            <h4 className="card-title text-center">Track</h4>
                            <p className="card-text">I'm full of tricks, baby, just like on Halloween.. A room full of monsters and it
                                makes me wanna scream. I have to get this right so you don't waste your time, not like my comedy,
                                I'm killing on this rhyme.</p>
                        </div>
                    </div>
                    <div className="card col-sm-4">
                        <i className="far fa-bookmark fa-5x text-center pt-4"></i>
                        <div className="card-body">
                            <h4 className="card-title text-center">Save</h4>
                            <p className="card-text">I'm gonna show you what I can do. You're going crazy and seeing two. It's not my
                                fault, you can't blame my game. <i>All these other hoes, but they're all the same.</i></p>
                        </div>
                    </div>
                </div>
            </div>
            <div className="d-flex justify-content-center p-4 blurb">
            <div className="col-3 text-center align-self-center"><i className="far fa-thumbs-up fa-10x"
                    style={{color: 'rgb(0, 0, 75)'}}></i></div>
            <div className="col-6">
                <p>"You're perfect, you're beautiful, you look like Linda Evangelista, you're a model! Everything about you is
                    perfect! Did you stone those tights? Oh, you're smiling!" They eat her up EVERY SINGLE TIME she's on that
                    damned
                    stage."
                </p>
                <p>She could walk out there in a ducking diaper and they'd be like, <strong><i>'Valentina! Your smile is
                            beautiful!'"</i></strong>
                </p>
            </div>
        </div>
            <footer className="page-footer font-small sticky-bottom">
            <div className="container">
                <div className="row">
                    <div className="col-md-12 pt-5 pb-2">
                        <div className="mb-5 text-center">
                            <a className="fb-ic">
                                <i className="fab fa-facebook-f fa-lg white-text mr-md-5 mr-3 fa-2x"> </i>
                            </a>
                            <a className="tw-ic">
                                <i className="fab fa-twitter fa-lg white-text mr-md-5 mr-3 fa-2x"> </i>
                            </a>
                            <a className="gplus-ic">
                                <i className="fab fa-google-plus-g fa-lg white-text mr-md-5 mr-3 fa-2x"> </i>
                            </a>
                            <a className="li-ic">
                                <i className="fab fa-linkedin-in fa-lg white-text mr-md-5 mr-3 fa-2x"> </i>
                            </a>
                            <a className="ins-ic">
                                <i className="fab fa-instagram fa-lg white-text mr-md-5 mr-3 fa-2x"> </i>
                            </a>
                            <a className="pin-ic">
                                <i className="fab fa-pinterest fa-lg white-text fa-2x"> </i>
                            </a>
                        </div>
                    </div>
                </div>
            </div>


            <div className="footer-copyright text-center py-1">© 2020 Copyright staple-team
            </div>

        </footer>
        </div>    
    
    )
}

export default Landing;