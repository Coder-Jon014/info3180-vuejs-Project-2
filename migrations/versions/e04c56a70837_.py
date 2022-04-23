"""empty message

Revision ID: e04c56a70837
Revises: 8cc5f686814b
Create Date: 2022-04-23 04:35:35.518171

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e04c56a70837'
down_revision = '8cc5f686814b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Cars', sa.Column('imageee', sa.String(length=80), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Cars', 'imageee')
    # ### end Alembic commands ###
