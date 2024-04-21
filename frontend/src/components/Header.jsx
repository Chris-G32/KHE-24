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
            <UserButton />
        </SignedIn>
    </header>
    )    
}

function Logo() {
    return (
        <h1 className='header_logo'>
            Logo
        </h1>
    )
}

export {
    Header
}