import React from 'react';
import { Link } from 'react-router-dom';

const Header = () => {
  return (
    <header className="bg-[var(--primary-blue)] text-white py-4">
      <div className="container mx-auto px-4 sm:px-6 lg:px-8 flex justify-between items-center">
        <div className="flex items-center">
          <Link to="/" className="text-2xl font-bold">
            FullStack SMSTS
          </Link>
          <span className="ml-2 text-sm bg-[var(--orange-accent)] px-2 py-1 rounded">
            CITB Accredited
          </span>
        </div>
        
        <div className="flex items-center space-x-4">
          <a 
            href="tel:01234567890" 
            className="hidden md:flex items-center"
          >
            <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5 mr-2" viewBox="0 0 20 20" fill="currentColor">
              <path d="M2 3a1 1 0 011-1h2.153a1 1 0 01.986.836l.74 4.435a1 1 0 01-.54 1.06l-1.548.773a11.037 11.037 0 006.105 6.105l.774-1.548a1 1 0 011.059-.54l4.435.74a1 1 0 01.836.986V17a1 1 0 01-1 1h-2C7.82 18 2 12.18 2 5V3z" />
            </svg>
            01234 567 890
          </a>
          
          <Link 
            to="/book-course" 
            className="bg-[var(--cta-orange)] hover:bg-[var(--orange-accent)] text-white px-4 py-2 rounded-lg transition duration-150"
          >
            Book Now
          </Link>
        </div>
      </div>
    </header>
  );
};

export default Header;
