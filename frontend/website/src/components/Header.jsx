import './Header.css'
import { SignedIn, SignedOut, SignInButton, UserButton } from "@clerk/clerk-react";

function Header() {
    return (
    <header className='header'>
        <Logo />
        <SignedOut>
            <SignInButton className="signin"/>
        </SignedOut>
        <SignedIn>
            <UserButton className='user-btn' />
        </SignedIn>
    </header>
    )    
}

function Logo() {
    return (
        <h2 className='header_logo'>
            Scam Unlikely
        </h2>
    )
}

export {
    Header
}